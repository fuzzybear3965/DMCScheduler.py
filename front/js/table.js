a = doubleClickHandler();

var table = new Tabulator('#table', {
    layout: 'fitColumns',
    index: 'First',
    columns: setColumns(),
    selectable: true,
    rowClick: a
})

var scheduleTable = new Tabulator('#schedule', {
    layout: 'fitColumns',
   columns: (function() {
            cols = [];
            cols.push({
                title: 'Name',
                field: 'name',
            })
            for (i = 0; i < 28; i++) {
                title_str = 'Day ' + i;
                field_str = 'day' + i;
                cols.push({
                    title: title_str,
                    field: field_str,
                    align: 'center',
                    bottomCalc: 'count',
                    formatter: function(cell, params, onRendered) {
                        if (cell.getValue().match(/7[A|P]C/) !== null) {
                            cell.getElement().style.background = '#FFC0CB';
                        }
                        return cell.getValue();
                    },
                }); 
            }
            return cols
        }()),
})

function setColumns() {
    var fields = ['First','Last','Seniority','Title','WeekendType','Charge','Vent','RequestedOn',
    'RequestedOff','RequestedOffSchool','Vacation','Education','Bonus'];
    cols = fields.map(x => ({field: x}))
    
    for (col of cols) {
        f = col.field
        if ( f === 'First' || f === 'Last' || f === 'Seniority') {
            col.editor = true;
        }  else if ( f === 'Title' ) {
            col.editor = 'select';
            col.editorParams = {Nurse: 'Nurse', CNA: 'CNA'};
        } else if ( f === 'WeekendType') {
            col.editor = 'select';
            col.editorParams = {'A': 'A', 'B': 'B'};
        } else if (f === 'Charge' || f === 'Vent') {
            col.editor = 'select';
            col.editorParams= {Yes:'Yes', No: 'No'};
        }else if (
            f === 'RequestedOn' || f === 'RequestedOff' ||
            f === 'RequestedOffSchool' || f === 'Vacation' ||
            f === 'Education' || f === 'Bonus'){
            col.editor = true;
        } 
        col.title = f;
    }
    return cols
}

function insertTable(d) {
    table.setData(d.data);
}

function insertSchedule(d) {
    scheduleTable.setData(d);
}

function addRow() { table.addRow({}) }

var addRowEl = document.getElementById('add-row');
addRowEl.addEventListener('click', addRow)

function doubleClickHandler() {
    var clickedStruct = [];
    return function(e,row) {
        console.log(row)
        console.log(e)
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
