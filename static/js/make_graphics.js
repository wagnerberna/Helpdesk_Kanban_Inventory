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

async function pie_tasks_projects(url) {
    const data = await fetch_url(url)
    console.log(data)

    const ctx = document.getElementById('pie_tasks_projects').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: data.labels,
            datasets: [
                {
                    label: "Projetos",
                    data: data.tasks_total,
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