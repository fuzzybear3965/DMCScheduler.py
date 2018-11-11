doubleClickState = doubleClickHandler();

// Create Tabulator object
var table = new Tabulator('#table', {
    layout: 'fitColumns',
    index: 'First',
    columns: setColumns(),
    selectable: false,
    rowClick: doubleClickState,
})

// Configure the columns for table mode
function setColumns() {
    var fields = ['First','Last','Seniority','WeekendType','VacationType','Charge','Vent'];
    cols = fields.map(x => ({field: x}))

    for (col of cols) {
        col.editor = dataEditor;
        f = col.field
        col.title = f;
        if ( f === 'First' || f === 'Last' || f === 'Seniority') {
            col.width='100';
            col.editor = true;
        } else if ( f === 'WeekendType') {
            col.editor = 'select';
            col.editorParams = {values: ["A", "B"]}
            col.width = '100';
            col.title = 'Weekend';
        } else if ( f === 'VacationType') {
            col.editor = 'select';
            col.editorParams = {values: ["A", "B", "C"]}
            col.title = 'Vacation';
            col.width = '100';
        } else if (f === 'Charge' || f === 'Vent') {
            col.editor = 'select';
            col.editorParams = {values: ["Yes", "No"]};
            col.width='80';
        }

    }
    for (i = 0; i < 28; i++) {
        title_str = `${i}`;
        field_str = title_str;
        cols.push({
            title: title_str,
            field: field_str,
            editor: 'select',
            editorParams : {values: ['', '7P', '7$P', 'RO', 'ROS', 'EDU', 'VAC',]}, 
        });
        col.editor = 'select';
    }
    for (col of cols) {
        col.editable = isEditable;
    }

    return cols
}

function dataEditor(cell, onRendered, success, cancel, editorParam) {

}
// Configure row adding capabilities
function addRow() { table.addRow({}) }

var addRowEl = document.getElementById('add-row');
addRowEl.addEventListener('click', addRow)

// Helper function to handle deleting rows
function doubleClickHandler() {
    var clickedStruct = [];
    return function(e,row) {
        var found = false;
        var rowObj =  {row:row, cnt: 0}
        for (var i = 0; i < clickedStruct.length; i++) {
            if (clickedStruct[i].row.getPosition() === row.getPosition()) {
                found = true;
                rowObj = clickedStruct[i]
            }
        }

        rowObj.cnt += 1;
        if (rowObj.cnt === 1) {
            rowObj.timer = setTimeout(function() {
                rowObj.cnt = 0;
            }, 400);
        } else if (rowObj.cnt === 2) {
            rowObj.timer = clearTimeout(rowObj.timer)
            rowObj.row.delete()
        }

        if (found === false) {
            clickedStruct.push(rowObj);
        }
    }
}

// Allow for user to change the editability of the page
var toggleEditEl = document.getElementById('toggle-editability');
toggleEditEl.addEventListener('click', toggleEditability)

function toggleEditability() {
    noteEl = document.getElementById('note-if-editable');
    var isEditable = (noteEl.innerText === '(Currently Editable)') ? true : false;
    if (isEditable) {
        noteEl.innerText = '(Currently Not Editable)';
    } else {
        noteEl.innerText = '(Currently Editable)';
    }
}

function isEditable() {
    noteEl = document.getElementById('note-if-editable');
    return (noteEl.innerText === '(Currently Editable)') ? true : false;
}

// Add Download feature
function downloadTemplate(e) {
    table.download('csv', 'schedule-template-' + timeStamp() + '.csv', {'delimiter':'|'})
}

dlEl = document.getElementById('download')
dlEl.addEventListener('click', downloadTemplate)

function insertTable(d) {
    table.setData(d.data);
}
