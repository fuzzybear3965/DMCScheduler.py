var scheduleTable = new Tabulator('#schedule', {
    layout: 'fitColumns',
   columns: (function() {
            cols = [];
            cols.push({
                title: 'Name',
                field: 'name',
            })
            for (i = 0; i < 28; i++) {
                var day = '';
                switch (i%7) {
                    case 0:
                        day = 'Su';
                        break;
                    case 1:
                        day = 'M';
                        break;
                    case 2:
                        day = 'T';
                        break;
                    case 3:
                        day = 'W';
                        break;
                    case 4:
                        day = 'R';
                        break;
                    case 5:
                        day = 'F';
                        break;
                    case 6:
                        day = 'Sa';
                        break;
                }
                week = Math.floor(i/7);

                title_str = day + ' ' + week + ' (' + i + ')';
                field_str = 'day' + i;
                cols.push({
                    title: title_str,
                    field: field_str,
                    align: 'center',
                    bottomCalc: 'count',
                    formatter: function(cell, params, onRendered) {
                        pastel_red = '#FFC0CB';
                        pastel_blue = '#AEC6CF';
                        cell_value = cell.getValue();
                        if (cell.getValue() === '7P(C)') {
                            cell.getElement().style.background = pastel_red;
                        } else if (cell.getValue() === '7P(V)') {
                            cell.getElement().style.background = pastel_blue;
                        } else if (cell.getValue() === '7P(C)(V)') {
                            cell.getElement().style.background = `linear-gradient(to right, ${pastel_red} 50%, ${pastel_blue} 50%)`;
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
