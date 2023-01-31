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


function buscaGulosa (start,graph,end,heur) { 
        
    const newOpenedNodes = (name) =>{
        const neighbourKeys = Object.keys(graph.get(name))
         
        return neighbourKeys
    }
    const getObjectKey = (obj, value) => {
        return Object.keys(obj).find((key) => obj[key] === value);
    }
    const caminho = (listafechados,heur) =>{
        const obj = {}
        for (const key of listafechados) { obj[key] = heur[key] }
        return obj
    }

    const listaAbertos = []
    const listafechados = []
    listaAbertos.push(...newOpenedNodes(start))
    listafechados.push(start)
    while (listaAbertos.length > 0 && !listafechados.includes(end) ) {
        const leafes = {}
        for (const key of listaAbertos) { leafes[key] = heur[key] }
        const minHeur = Math.min(...Object.values(leafes))
        const minHeurKey = getObjectKey(leafes,minHeur)
        listafechados.push( ...listaAbertos.splice(listaAbertos.indexOf(minHeurKey),1) )
        listaAbertos.push(...newOpenedNodes(minHeurKey).filter(d => !listaAbertos.includes(d) && !listafechados.includes(d) ))                
        
        //console.log(listaAbertos) //getObjectKey(leafes,minHeur)
        //console.log(listafechados)
    }
    return caminho(listafechados,heur)

}


 console.log('Melhor caminho na busca gulosa',buscaGulosa('A',labGraph,'G',heuristica))