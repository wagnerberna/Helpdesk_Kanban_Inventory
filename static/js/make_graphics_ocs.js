function fetch_url(url) {
    console.log(url)
    console.log("!!!Teste JS!!!")
    // console.log(data)
    return fetch(url, { method: "get" }).then(data => data.json())
}

async function ocs_pie_general(url) {
    const data = await fetch_url(url)

    const ctx = document.getElementById('ocs_pie_cpu').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: data.cpu_names,
            datasets: [
                {
                    label: "Ranking Workstations",
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

    const ctx = document.getElementById('ocs_pie_cpu').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: data.cpu_names,
            datasets: [
                {
                    label: "Ranking Workstations",
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