function fetch_url(url) {
    // console.log(url)
    return fetch(url, { method: "get" }).then(data => data.json())
}

async function bar_demands_by_technical(url) {
    const data = await fetch_url(url)

    const ctx = document.getElementById('bar_demands_by_technical').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [
                {
                    label: "Chamados por Técnico",
                    data: data.data,
                    backgroundColor: [
                        '#7fe686',
                    ],
                    borderColor: [
                        '#2ad535',
                    ],
                    borderWidth: 1
                },
            ]

        },
    });
}

async function bar_tasks_by_technical(url) {
    const data = await fetch_url(url)

    const ctx = document.getElementById('bar_tasks_by_technical').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [
                {
                    label: "Tarefas de Projetos por Técnico",
                    data: data.data,
                    backgroundColor: [
                        '#86cbf9',
                    ],
                    borderColor: [
                        '#0b97f4',
                    ],
                    borderWidth: 1
                },
            ]

        },
    });
}

async function bar_tasks_status_project(url) {
    const data = await fetch_url(url)

    const ctx = document.getElementById('bar_tasks_status_project').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [
                {
                    label: data.label_status[0],
                    data: data.tasks_to_do,
                    backgroundColor: [
                        '#7fe686',
                    ],
                    borderColor: [
                        '#2ad535',
                    ],
                    borderWidth: 1
                },
                {
                    label: data.label_status[1],
                    data: data.tasks_doing,
                    backgroundColor: [
                        '#ffe97f',
                    ],
                    borderColor: [
                        '#ffd500',
                    ],
                    borderWidth: 1
                },
                {
                    label: data.label_status[2],
                    data: data.tasks_blocked,
                    backgroundColor: [
                        '#fe7167',
                    ],
                    borderColor: [
                        '#fe1201',
                    ],
                    borderWidth: 1
                },
                {
                    label: data.label_status[3],
                    data: data.tasks_done,
                    backgroundColor: [
                        '#86cbf9',
                    ],
                    borderColor: [
                        '#0b97f4',
                    ],
                    borderWidth: 1
                },
            ]

        },
    });
}

async function pie_tasks_projects(url) {
    const data = await fetch_url(url)
    // console.log(data)

    const ctx = document.getElementById('pie_tasks_projects').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: data.labels,
            datasets: [
                {
                    label: "Total de Tarefas",
                    data: data.tasks_total,
                    backgroundColor: [
                        '#86cbf9',
                        '#7fe686',
                        '#ffe97f',
                        '#fe7167',
                        '#ff80ff',
                        '#80ffff',
                        '#ffcc80',
                        '#ff9f80',
                        '#ccccb3',
                        '#b3cccc',
                    ],
                    borderColor: [
                        '#0b97f4',
                        '#2ad535',
                        '#ffd500',
                        '#fe1201',
                        '#ff00ff',
                        '#00e6e6',
                        '#ff9900',
                        '#ff4000',
                        '#999966',
                        '#669999',
                    ],
                    borderWidth: 1
                },
            ]

        },
    });
}

async function bar_percentage_projects(url) {
    const data = await fetch_url(url)

    const ctx = document.getElementById('bar_percentage_projects').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [
                {
                    axis: "y",
                    label: "Percentual",
                    data: data.project_percentage,
                    backgroundColor: [
                        '#86cbf9',
                    ],
                    borderColor: [
                        '#0b97f4',
                    ],
                    borderWidth: 1
                },
            ]

        },
        options: {
            indexAxis: 'y',
            scales: {
                yAxes: [{
                    ticks: {
                        min: 0,
                        max: 120,
                        callback: function (value) { return value + "%" }
                    },
                    scaleLabel: {
                        display: true,
                        labelString: "Percentage"
                    }
                }]
            }
        }

    });
}

async function pie_workstations_ranking(url) {
    const data = await fetch_url(url)

    const ctx = document.getElementById('pie_workstations_ranking').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: data.labels,
            datasets: [
                {
                    label: "Ranking Workstations",
                    data: data.data,
                    backgroundColor: [
                        '#86cbf9',
                        '#7fe686',
                        '#ffe97f',
                        '#fe7167',
                        '#ff80ff',
                    ],
                    borderColor: [
                        '#0b97f4',
                        '#2ad535',
                        '#ffd500',
                        '#fe1201',
                        '#ff00ff',
                    ],
                    borderWidth: 1
                },
            ]

        },
    });
}

async function bar_workstations_ranking(url) {
    const data = await fetch_url(url)

    const ctx = document.getElementById('bar__workstations_ranking').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.departments_labels,
            datasets: [
                {
                    label: data.ranking_labels[0],
                    data: data.ranking_a,
                    backgroundColor: [
                        '#86cbf9',
                    ],
                    borderColor: [
                        '#0b97f4',
                    ],
                    borderWidth: 1
                },
                {
                    label: data.ranking_labels[1],
                    data: data.ranking_b,
                    backgroundColor: [
                        '#7fe686',
                    ],
                    borderColor: [
                        '#2ad535',
                    ],
                    borderWidth: 1
                },
                {
                    label: data.ranking_labels[2],
                    data: data.ranking_c,
                    backgroundColor: [
                        '#ffe97f',
                    ],
                    borderColor: [
                        '#ffd500',
                    ],
                    borderWidth: 1
                },
                {
                    label: data.ranking_labels[3],
                    data: data.ranking_d,
                    backgroundColor: [
                        '#fe7167',
                    ],
                    borderColor: [
                        '#fe1201',
                    ],
                    borderWidth: 1
                },
                {
                    label: data.ranking_labels[4],
                    data: data.ranking_e,
                    backgroundColor: [
                        '#ff80ff',
                    ],
                    borderColor: [
                        '#ff00ff',
                    ],
                    borderWidth: 1
                },
            ]
        },
    });
}