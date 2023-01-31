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

  

const heuristica = {'A':24,'B':15,'C':22,'D':12,'E': 7,'F':7, 'G':0 }


function aEstrela(start,graph,end,heur){
    const getObjectKey = (obj, value) => {
        return Object.keys(obj).find((key) => obj[key] === value);
    }
    const newOpenedNodes = (name) =>{
        const neighbourKeys = Object.keys(graph.get(name))
         
        return neighbourKeys
    }
    const iterateLeafes =(listaAbertos, heur)=>{
        const obj= {}
        for (const key of listaAbertos) {
            if(graph.get(...listaFechados.slice(-1))[key])
                obj[key] = heur[key] + graph.get(...listaFechados.slice(-1))[key]
        }
        return obj
    }

    const listaAbertos = []
    const listaFechados = []

    listaAbertos.push(...newOpenedNodes(start))
    listaFechados.push(start)
    while (listaAbertos.length > 0 && !listaFechados.includes(end) ) {
        const leafes = iterateLeafes(listaAbertos, heur)
        const candidate = Math.min(...Object.values(leafes))
        const candidateKey = getObjectKey(leafes,candidate)
        const indexDeleted = listaAbertos.indexOf(candidateKey)
        listaFechados.push(...listaAbertos.splice(indexDeleted,1))
        listaAbertos.push(...newOpenedNodes(candidateKey).filter(d => !listaAbertos.includes(d) && !listaFechados.includes(d)) )
    }

    return listaFechados
}


console.log(aEstrela('A',labGraph,'G',heuristica))