a = doubleClickHandler();

// Create Tabulator object
var table = new Tabulator('#table', {
    layout: 'fitColumns',
    index: 'First',
    columns: setColumnsForTableMode(),
    selectable: true,
    rowClick: a,
})

// Configure the columns for list mode
function setColumnsForListMode() {
    var fields = ['First','Last','Seniority','WeekendType','Charge','Vent','RequestedOn',
    'RequestedOff','RequestedOffSchool','Vacation','Education','Bonus'];
    cols = fields.map(x => ({field: x}))

    for (col of cols) {
        f = col.field
        if ( f === 'First' || f === 'Last' || f === 'Seniority') {
            //col.editor = editable;
            col.title = f;
        } else if ( f === 'WeekendType') {
            //if (editable) {
                //col.editor = 'select';
                //col.editorParams = {'A': 'A', 'B': 'B'};
            //}
            col.title = 'Weekend';
        } else if (f === 'Charge' || f === 'Vent') {
            //if (editable) {
                //col.editor = 'select';
                //col.editorParams= {Yes:'Yes', No: 'No'};
            //}
            col.title = f;
        } else if (
            f === 'RequestedOn' || f === 'RequestedOff' ||
            f === 'RequestedOffSchool' || f === 'Vacation' ||
            f === 'Education' || f === 'Bonus') {
            //col.editor = editable;
            switch (f) {
                case 'RequestedOn':
                    col.title = 'Requested';
                    break;
                case 'RequestedOff':
                    col.title = 'RO';
                    break;
                case 'RequestedOffSchool':
                    col.title = 'ROS';
                    break;
                case 'Vacation':
                    col.title = 'VAC';
                    break;
                case 'Education':
                    col.title = 'EDU';
                    break;
                case 'Bonus':
                    col.title = 'Bonus';
                    break;
            }
        }
    }
    return cols
}

// Configure the columns for table mode
function setColumnsForTableMode() {
    var fields = ['First','Last','Seniority','WeekendType','VacationType','Charge','Vent'];
    cols = fields.map(x => ({field: x}))

    for (col of cols) {
        col.editor = dataEditor;
        f = col.field
        col.title = f;
        if ( f === 'First' || f === 'Last' || f === 'Seniority') {
            col.width='100';
        } else if ( f === 'WeekendType') {
            //col.editor = 'select';
            //col.editorParams = {'A': 'A', 'B': 'B'};
            col.width = '100';
            col.title = 'Weekend';
        } else if ( f === 'VacationType') {
            //col.editor = 'select';
            //col.editorParams = {'A': 'A', 'B': 'B', 'C': 'C'};
            col.title = 'Vacation';
            col.width = '100';
        } else if (f === 'Charge' || f === 'Vent') {
            //if (editable) {
                //col.editor = 'select';
                //col.editorParams= {Yes:'Yes', No: 'No'};
            //}
            col.width='80';
        }

    }
    for (i = 0; i < 28; i++) {
        var day = i;

        title_str = `${i}`;
        field_str = title_str;
        cols.push({
            title: title_str,
            field: field_str,
        }); 
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

// Add Download feature
function downloadTemplate(e) {
    table.download('csv', 'schedule-template-' + timeStamp() + '.csv', {'delimiter':'|'})
}

dlEl = document.getElementById('download')
dlEl.addEventListener('click', downloadTemplate)

function dayString(i) {
            switch (i%7) {
                case 0:
                    return 'Su';
                case 1:
                    return 'M';
                case 2:
                    return 'T';
                case 3:
                    return 'W';
                case 4:
                    return 'R';
                case 5:
                    return 'F';
                case 6:
                    return 'Sa';
            }
}

function insertTable(d) {
    table.setData(d.data);
}

// Allow for user to change table modes
var tableFormatEl = document.getElementById('list-or-table');
tableFormatEl.addEventListener('click', changeTableFormat)

function changeTableFormat() {
    var curState  = document.getElementById('note-table-format').innerText;
    var isTableMode = (curState === '(Currently in Table Mode)') ? true : false;
    if (isTableMode) {
        document.getElementById('note-table-format').innerText = '(Currently in List Mode)';
        table.setColumns(setColumnsForListMode());
    } else {
        document.getElementById('note-table-format').innerText = '(Currently in Table Mode)';
        table.setColumns(setColumnsForTableMode());
    }
}
