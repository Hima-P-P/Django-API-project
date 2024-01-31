from books.models import Books
from rest_framework.decorators import api_view
from books.serializers import bookserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins,generics,viewsets
from books.serializers import User
from books.serializers import userserializer
from rest_framework.permissions import IsAuthenticated


# @api_view(['GET','POST'])
# def booklist(request):  #non primary key
#     if(request.method=="GET"):
#         books=Books.objects.all()  #django format data
#         b=bookserializer(books,many=True)  #convert into json format
#         return Response(b.data)  #json data response
#     elif(request.method=="POST"): #new record create
#         b=bookserializer(data=request.data) #deserialization process-cient data included
#         if b.is_valid():  #checks for valid or not
#             b.save()
#             return Response(b.data,status=status.HTTP_201_CREATED)
#     return Response(b.errors,status=status.HTTP_480_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def book_detail(request,pk): #primary key based
#     try:
#         book=Books.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if(request.method=="GET"):
#         b=bookserializer(book) #serialization
#         return Response(b.data)
#     elif(request.method=="PUT"):   
#        b=bookserializer(book,data=request.data)  #deserialization--updated data saved to student
#        if b.is_valid():
#            b.save()
#            return Response(b.data,status=status.HTTP_201_CREATED)
#        return Response(b.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif(request.method=="DELETE"):
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#mixins
# class booklist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView): #non primary key based
#     queryset=Books.objects.all()
#     serializer_class=bookserializer
#     def get(self,request):
#      return self.list(request)
#     def post(self,request):
#      return self.create(request)
    
# class bookdetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):primary key based
#     queryset=Books.objects.all()
#     serializer_class=bookserializer
#     def get(self,request,pk):
#      return self.retrieve(request)
#     def put(self,request,pk):
#      return self.update(request)
#     def delete(self,request,pk):
#      return self.destroy(request)
    

#generic
# class booklist(generics.ListCreateAPIView): #non primary key based
#     queryset=Books.objects.all()
#     serializer_class=bookserializer
    
    
# class bookdetail(generics.RetrieveUpdateDestroyAPIView):#primary key based
#     queryset=Books.objects.all()
#     serializer_class=bookserializer
    
#viewset
class bookviewset(viewsets.ModelViewSet) : #primary key and non primary key based
  permission_classes=[IsAuthenticated,]
  queryset=Books.objects.all()
  serializer_class=bookserializer


#viewset-registerapiview
class userviewset(viewsets.ModelViewSet) : #primary key and non primary key based
  queryset=User.objects.all()
  serializer_class=userserializer
