# def upload_success(request):
#     # request.FILES : enctype으로 전소오디어 온 파일 파라미터 객체
#     # .name 등의 파일의 정보를 받을 수 있다.
#     if 'file1' in request.FILES:
#         # 파라미터 처리
#         file = request.FILES['file1']
#         file_name = file.name  # 첨부파일 이름
#
#         # 파일 오픈 - wb모드(binary)
#         fp = open("%s%s" % (MEDIA_URL, file_name), 'wb')
#
#         # 파일을 1바이트씩 조금씩 읽어서 저장
#         for chunk in file.chunks():
#             fp.write(chunk)
#         fp.close()  # 파일 닫기
#
#     else:
#         file_name = '-'
#     return render(request, "image/success.html", {'file_name': file_name})


# def index(request):
#     return render(request, "image/index.html")


# def upload(request):
#     context = {}
#     if request.method == 'POST':
#         # if (request.FILES['uploadBtn']):
#         #     uploaded_file = request.FILES['uploadBtn']
#         # elif (request.FILES['myFile']):
#         uploaded_file = request.FILES.get('uploadBtn', None)
#         filesys = FileSystemStorage()
#         name = filesys.save(uploaded_file.name, uploaded_file)
#         #context['url'] = filesys.url(name)
#         context = filesys.url(name)
#     return render(request, 'image/index.html', context)

# def upload(request):
#     if 'uploadBtn' in request.FILES:
#         post = request.FILES['uploadBtn']
#         file_name = post.name
#         fp = open("%s%s" % (MEDIA_URL, file_name), 'wb')
#
#         for chunk in post.chunks():
#             fp.write(chunk)
#         fp.close()
#     else:
#         file_name = '-'
#     return render(request, "image/index.html", {'file_name': file_name})