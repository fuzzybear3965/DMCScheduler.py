a = doubleClickHandler();

var table = new Tabulator('#table', {
    layout: 'fitColumns',
    index: 'First',
    columns: setColumns(true),
    selectable: true,
    rowClick: a
})

function setColumns(editable) {
    var fields = ['First','Last','Seniority','WeekendType','Charge','Vent','RequestedOn',
    'RequestedOff','RequestedOffSchool','Vacation','Education','Bonus'];
    cols = fields.map(x => ({field: x}))

    for (col of cols) {
        f = col.field
        if ( f === 'First' || f === 'Last' || f === 'Seniority') {
            col.editor = editable;
        } else if ( f === 'WeekendType') {
            if (editable) {
                col.editor = 'select';
                col.editorParams = {'A': 'A', 'B': 'B'};
            }
        } else if (f === 'Charge' || f === 'Vent') {
            if (editable) {
                col.editor = 'select';
                col.editorParams= {Yes:'Yes', No: 'No'};
            }
        }else if (
            f === 'RequestedOn' || f === 'RequestedOff' ||
            f === 'RequestedOffSchool' || f === 'Vacation' ||
            f === 'Education' || f === 'Bonus'){
            if (editable) {
                col.editor = true;
            }
        }
        col.title = f;
    }
    return cols
}

function insertTable(d) {
    table.setData(d.data);
}

function addRow() { table.addRow({}) }

var addRowEl = document.getElementById('add-row');
addRowEl.addEventListener('click', addRow)

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

var toggleEditEl = document.getElementById('toggle-editability');
toggleEditEl.addEventListener('click', toggleEditability)

function toggleEditability() {
    var isEditable = table.columnManager.columns[0].definition.editor;
    noteEl = document.getElementById('note-if-editable');
    noteEl.innerText = !isEditable ? '(Currently Editable)' : '(Currently Not Editable)';
    table.setColumns(setColumns(!isEditable));
}

function downloadTemplate(e) {
    table.download('csv', 'schedule-template-' + timeStamp() + '.csv', {'delimiter':'|'})
}

dlEl = document.getElementById('download')
dlEl.addEventListener('click', downloadTemplate)
