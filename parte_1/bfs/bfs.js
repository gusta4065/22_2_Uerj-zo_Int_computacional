const lab = new Map()

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

console.log(lab)

function bfSearch(start) {
    const visited = new Set();
    const queue = [start];
    visited.add(start)
    while (queue.length > 0) {
        
        const labyrinth = queue.shift();
        const destinations = lab.get(labyrinth)
        
        for (const destination of destinations) {
        
            if(destination === 'S'){
                console.log('encontrado')
                visited.add(destination)
                break
            }
            if(!visited.has(destination)){
                visited.add(destination)
                queue.push(destination)
            }
        }
    }
    console.log(visited)
}

bfSearch('A')