function fetch_url(url) {
    // console.log(url)
    return fetch(url, { method: "get" }).then(data => data.json())
}

async function bar_demands_by_technical(url) {
    const data = await fetch_url(url)
    // console.log(data)
    // console.log(data.labels[0])
    // console.log(data.data[0])

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
                        'rgba(255, 99, 132, 0.2)',
                    ],
                    borderColor: [
                        'rgb(255, 99, 132)',
                    ],
                    borderWidth: 1
                },
            ]

        },
    });
}

async function bar_tasks_by_technical(url) {
    const data = await fetch_url(url)
    console.log(data)
    console.log(data.labels[1])
    console.log(data.data[1])

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
                        'rgba(255, 99, 132, 0.2)',
                    ],
                    borderColor: [
                        'rgb(255, 99, 132)',
                    ],
                    borderWidth: 1
                },
            ]

        },
    });
}