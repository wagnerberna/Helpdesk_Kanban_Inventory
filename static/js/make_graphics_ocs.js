function fetch_url(url) {
    console.log(url)
    // console.log("!!!Teste JS!!!")
    // console.log(data)
    return fetch(url, { method: "get" }).then(data => data.json())
}

async function ocs_pie_cpu(url) {
    const data = await fetch_url(url)

    const ctx = document.getElementById('ocs_pie_cpu').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: data.cpu_labels,
            datasets: [
                {
                    label: "Estações de Trabalho por CPU",
                    data: data.cpu_counts,
                    backgroundColor: [
                        '#86cbf9',
                        '#7fe686',
                        '#ffe97f',
                        '#fe7167',
                    ],
                    borderColor: [
                        '#0b97f4',
                        '#2ad535',
                        '#ffd500',
                        '#fe1201',
                    ],
                    borderWidth: 1
                },
            ]

        },
    });
}

async function ocs_pie_memory(url) {
    const data = await fetch_url(url)

    const ctx = document.getElementById('ocs_pie_memory').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: data.memory_labels,
            datasets: [
                {
                    label: "Estações de Trabalho por Memória",
                    data: data.memory_counts,
                    backgroundColor: [
                        '#86cbf9',
                        '#7fe686',
                        '#ffe97f',
                        '#fe7167',
                    ],
                    borderColor: [
                        '#0b97f4',
                        '#2ad535',
                        '#ffd500',
                        '#fe1201',
                    ],
                    borderWidth: 1
                },
            ]

        },
    });
}