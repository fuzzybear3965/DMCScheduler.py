var table = new Tabulator('#table', {
    layout: 'fitColumns',
    index: 'First',
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
