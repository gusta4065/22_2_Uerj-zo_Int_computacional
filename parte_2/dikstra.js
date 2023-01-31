const labGraph = new Map()

labGraph.set('A',{
    'B': 9,
    'C': 5,
    'D': 13
});
labGraph.set('B',{
    'A': 9,
    'D': 3,
    'E': 10
});
labGraph.set('C',{
    'A': 5,
    'F': 12
});
labGraph.set('D',{
    'A': 13,
    'B': 3,
    'E': 6,
    'G': 14
});
labGraph.set('E',{
    'B': 10,
    'D': 6,
    'G': 7
});
labGraph.set('F',{
    'C': 12,
    'G': 10
});
labGraph.set('G',{
    'D': 14,
    'E': 7,
    'G': 10
});


const dijskstra = (graph, start, end)=>{
// funçoes pra iterar as lista
    const iterateUnvisited = ()=>{ //lista de nós abertos
        const node = []
        for (const [key, value] of graph) { node.push(key) }
        const obj = {}
        for (const n of node) {
            obj[n] = 999999999
        }
        obj[start] = 0
        return obj
    }
    const iterateCandidate = ()=>{ //encontrando o candidato
        function getObjectKey(obj, value) {
            return Object.keys(obj).find((key) => obj[key] === value);
        }
        const minValue = Math.min(...Object.values(unvisited)) // pegando o valor minimo dos grafos
        const minKey = getObjectKey(unvisited,minValue )
        //return {[minKey]: minValue}
        return minKey
    }
// o algoritimo de fato
    const visited = {}
    const parents = {}
    const unvisited = iterateUnvisited() // lista de vertices visditrados
    while(Object.keys(unvisited).length){
        const minVertx = iterateCandidate()  // pega menor vertice 
        for (const neighbour of Object.keys(graph.get(minVertx))) {
            if (Object.keys(visited).includes(neighbour)) continue
            const distance = unvisited[minVertx] + graph.get(minVertx)[neighbour]
            if(distance < unvisited[neighbour]){
                unvisited[neighbour] = distance
                parents[neighbour] = minVertx
            }
        }
        visited[minVertx] = unvisited[minVertx]
        //delete unvisited[Object.keys(unvisited)[0]]
        delete unvisited[minVertx]
    }
    return visited//'dijsktra'
}

console.log(dijskstra(labGraph,'A','G'))