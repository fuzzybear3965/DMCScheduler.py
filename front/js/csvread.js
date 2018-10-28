// The following taken from https://www.html5rocks.com/en/tutorials/file/dndfiles/
// Check for the various File API support.
if (window.File && window.FileReader && window.FileList && window.Blob) {
    // Great success! All the File APIs are supported.
    function handleFileSelect(evt) {
        var file = evt.target.files[0]; // FileList object

        // files is a FileList of File objects. List some properties.
        var reader = new FileReader();
        reader.onload = (function(f) {
            return function(e) {
                Papa.parse(f, {
                    delimiter: "|",
                    header: true,
                    complete: insertTable,
                    skipEmptyLines: true,
                })
            }
        })(file)

        reader.readAsText(file);

        var output = (
            '<li><strong>', escape(file.name), '</strong> </li>'
        );

        document.getElementById('list').innerHTML = '<ul>' + output + '</ul>';
    }

    document.getElementById('file').addEventListener('change', handleFileSelect, false);

    function insertTable(d) {
        var table = new Tabulator('#table', {
            layout: 'fitColumns',
            index: 'First',
            data: d.data,
            columns: (function() {
            })(),
        });

        //table.setData(data)
            //.then(function() {

            //})
            //.catch(function(e){
                //console.log(e);
            //});
    }

} else {
    alert('The File APIs are not fully supported in this browser.');
}
