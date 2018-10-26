// The following taken from https://www.html5rocks.com/en/tutorials/file/dndfiles/
// Check for the various File API support.
if (window.File && window.FileReader && window.FileList && window.Blob) {
    // Great success! All the File APIs are supported.
    function handleFileSelect(evt) {
        var file = evt.target.files[0]; // FileList object
        console.log(evt.target)

        // files is a FileList of File objects. List some properties.
        var reader = new FileReader();
        reader.onload = (function(f) {
            return function(e) {
                Papa.parse(f, {
                    delimiter: "|",
                    header: true,
                    complete: addStaffToDOM,
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

    function addStaffToDOM(results, file) {
        ws.send(JSON.stringify(results));

        var body = document.body;
        var header = results.meta.fields;
        for (row of results.data) {
            var staffEl = document.createElement('p');
            for (item of header) {
                var cell = document.createElement('span');
                cell.classList.add("col-" + header.indexOf(item));
                cell.innerText = row[item];
                staffEl.appendChild(cell);
                body.appendChild(staffEl);
            }
        }
    }

} else {
    alert('The File APIs are not fully supported in this browser.');
}
