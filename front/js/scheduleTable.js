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

function insertSchedule(d) {
    scheduleTable.setData(d);
}
