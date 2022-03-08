$(document).ready(function(){
        $('#uploadBtn').change(function(e){
            console.log(this.files);
            document.getElementById("uploadFile").value = this.files[0].name;
            document.getElementById("size").innerText = getsize(this.files[0].size)
        });
    });

function getsize(file) {
    const size = file / 1048576;
    const size_round = Math.round(size);
    return size_round + 'MB';
}