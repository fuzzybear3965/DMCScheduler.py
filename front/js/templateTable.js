// Create Tabulator object
var table = new Tabulator('#table', {
    layout: 'fitColumns',
    index: 'First',
    columns: setColumns(),
    selectable: false,
})

// Configure the columns for table mode
function setColumns() {
    var fields = ['First','Last','Seniority','WeekendType','VacationType','Charge','Vent'];
    cols = fields.map(x => ({field: x}))

    for (col of cols) {
        f = col.field
        if ( f === 'First' || f === 'Last' || f === 'Seniority') {
            col.width='100';
            col.editor = true;
            col.title = f;
        } else if ( f === 'WeekendType') {
            col.editor = 'select';
            col.editorParams = {values: ["A", "B"]}
            col.width = '100';
            col.title = 'Weekend';
            col.downloadTitle = f;
        } else if ( f === 'VacationType') {
            col.editor = 'select';
            col.editorParams = {values: ["A", "B", "C"]}
            col.width = '100';
            col.title = 'Vacation';
            col.downloadTitle = f;
        } else if (f === 'Charge' || f === 'Vent') {
            col.editor = 'select';
            col.editorParams = {values: ["Yes", "No"]};
            col.width='80';
            col.title = f;
        }

    }
    for (i = 0; i < 28; i++) {
        title_str = `${i}`;
        field_str = title_str;
        col_obj = {
            title: title_str,
            field: field_str,
            editor: 'select',
            editorParams : {values: ['7P', '7$P', 'RO', 'ROS', 'EDU', 'VAC']},
            }
        }
        if (i%7===0||i%7===6) {
            col_obj.cssClass = "grey";
        }
        cols.push(col_obj);
    }
    for (col of cols) {
        col.editable = isEditable;
        col.cellDblClick = function(e, cell) {
            if (!isEditable()) {
                let row = cell.getRow();
                row.delete();
            }
        }
    }

    return cols
}

// Configure row adding capabilities
function addRow() { table.addRow({}) }

var addRowEl = document.getElementById('add-row');
addRowEl.addEventListener('click', addRow)

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
