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

            title_str = `${i}`;
            field_str = `day${i}`;
            col_obj = {
                title: title_str,
                field: field_str,
                align: 'center',
                bottomCalc: 'count',
                formatter: cellFormatter,
                editor: 'select',
                editorParams : {values: ['7P', '7$P', 'RO', 'ROS', 'EDU', 'VAC']}, 
            };
            if (i%7===0||i%7===6) {
                col_obj.cssClass = "grey";
            }
            cols.push(col_obj); 
        }
        return cols
    }()),
})

function insertSchedule(d) {
    // make sure page doesn't scroll to top
    x = document.documentElement.scrollLeft;
    y = document.documentElement.scrollTop;
    scheduleTable.setData(d);
    window.scrollTo(x,y);
}

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
