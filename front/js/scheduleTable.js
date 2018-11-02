var scheduleTable = new Tabulator('#schedule', {
    layout: 'fitColumns',
    columns: (function() {
        cols = [];
        cols.push({
            title: 'Name',
            field: 'name',
        })
        for (i = 0; i < 28; i++) {
            var day = dayString(i);

            title_str = `${day} (${i})`;
            field_str = 'day' + i;
            cols.push({
                title: title_str,
                field: field_str,
                align: 'center',
                bottomCalc: 'count',
                formatter: cellFormatter,
            }); 
        }
        return cols
    }()),
})

function insertSchedule(d) {
    scheduleTable.setData(d);
}

function downloadSchedule() {
    scheduleTable.download('pdf', 'generated-schedule-' + timeStamp() + '.pdf') 
}
downloadEl = document.getElementById('schedule-download');
downloadEl.addEventListener('click', downloadSchedule);

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

function cellFormatter(cell, params, onRendered) {
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
}
