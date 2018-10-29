var table = new Tabulator('#table', {
    layout: 'fitColumns',
    index: 'First',
})

var scheduleTable = new Tabulator('#schedule', {
    layout: 'fitColumns',
    //index: 'name',
})

function setColumns(data) {
    var cols = [];
    for (f of data.meta.fields) {
        col = {};
        if (f === 'Seniority') {
            col.editable = true;
        } else if (f === 'Charge' || f === 'Vent') {
            col.editor = 'select';
            col.editorParams= {Yes:'Yes', No: 'No'}
        } else if ( f === 'Title' ) {
            col.editor = 'select';
            col.editorParams = {Nurse: 'Nurse', CNA: 'CNA'}
        } else if (
            f === 'RequestedOn' || f === 'RequestedOff' ||
            f === 'RequestedOffSchool' || f === 'Vacation' ||
            f === 'Education' || f === 'Bonus'){
            col.editor = true;
        }
        col.title = f;
        col.field = f;
        cols.push(col);
    }
    return cols
}

function insertTable(d) {
    table.setData(d.data);
    table.setColumns(setColumns(d));
}

function insertSchedule(d) {
    scheduleTable.setData(d);
    scheduleTable.setColumns(
        (function() {
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
                }); 
            }
            return cols
        })()
    );
}
