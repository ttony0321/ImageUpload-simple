function setImageFromFile(input){
    if(input.files&&input.files[0]){
        var reader = new FileReader();
        reader.onload = function (e){
            $('#preview').removeClass('hide')
            $('#preimage').addClass('hide')
            $('#preview').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0])
    }
}

function CopyUrl(){
    var copy = document.getElementById('urlcopy');
    copy.select();
    document.execCommand('copy')
    copy.setSelectionRange(0,0);
    obj.setSelectionRange(0,0);

    // 선택영역 초기화
    var urlcopy = $('#urlcopy').val()
    console.log(urlcopy)
    // urlcopy.focus();
    // urlcopy.select();
    // document.execCommand('copy')
    console.log('copy complete')
}
//
// Dropzone.options.fileDropzone = {
//             url: '/media/',
//             headers: {'X-CSRFToken': '{{ csrf_token }}'},
//             init: function () {
//                 this.on("error", function (file, message) {
//                     alert(message);
//                     this.removeFile(file);
//                 });
//                 var submitBtn = document.querySelector("#submitBtn");
//                 var myDropzone = this;
//                 $("#submitBtn").on('click', function (){
//                     myDropzone.processQueue();
//                 })
//             },
//             autoProcessQueue: true,
//             method: "post",
//             clickable: true,
//             thumbnailHeight: 90,
//             thumbnailWidth: 115,
//             maxFiles: 1,
//             maxFilesize: 10,
//             parallelUploads: 1,
//             addRemoveLinks: true,
//             dictRemoveFile: 'delete',
//             uploadMultiple: false,
//
//         }