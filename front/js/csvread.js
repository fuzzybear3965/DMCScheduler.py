// The following taken from https://www.html5rocks.com/en/tutorials/file/dndfiles/
// Check for the various File API support.
if (window.File && window.FileReader && window.FileList && window.Blob) {
    // Great success! All the File APIs are supported.
    function handleFileSelect(evt) {
        var files = evt.target.files; // FileList object

        // files is a FileList of File objects. List some properties.
        var output = [];
        for (var i = 0, f; f = files[i]; i++) {
            var reader = new FileReader();
            reader.onload = (function(file) {
                return function(e) {
                    Papa.parse(file, {
                        delimiter: "|",
                        header: false,
                        complete: addStaffToDOM,
                    })
                }
            })(f);

            reader.readAsText(f);

            output.push(
                '<li><strong>',
                escape(f.name),
                '</strong> </li>');

            document.getElementById('list').innerHTML = '<ul>' + output.join('') + '</ul>';
        }
    }

    document.getElementById('files').addEventListener('change', handleFileSelect, false);

    function addStaffToDOM(results, file) {
        var body = document.body;
        for (row of results.data) {
            var staffEl = document.createElement('p');
            for (col of row) {
                var cell = document.createElement('span');
                cell.classList.add("cell");
                cell.innerText = col;
                staffEl.appendChild(cell);
            }
            body.appendChild(staffEl);
        }
    }

} else {
    alert('The File APIs are not fully supported in this browser.');
}

