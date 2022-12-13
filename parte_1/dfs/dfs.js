lab.set('A',['B','E'])
lab.set('B',['C','F'])
lab.set('C',['B'])
lab.set('D',['H'])
lab.set('E',['A','I'])
lab.set('F',['G','B'])
lab.set('G',['H','F','L'])
lab.set('H',['D'])
lab.set('I',['J','E','N'])
lab.set('J',['I','O'])
lab.set('L',['M','G'])
lab.set('M',['L','Q'])
lab.set('N',['I'])
lab.set('O',['P','J','R'])
lab.set('P',['O','Q','S'])
lab.set('Q',['P','M'])
lab.set('R',['O'])

function dfSearch(start, visited = new Set() ){
    console.log(start)
    visited.add(start)
    let destinations = lab.get(start)

    for (const destination of destinations) {
        if(destination === 'S'){
            console.log(`encontrado  em ${visited.size} passos`)
            
            return
        }
        if(!visited.has(destination)){
            dfSearch(destination,visited)
        }
    }

}


dfSearch('A')