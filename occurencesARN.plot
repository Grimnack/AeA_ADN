set terminal png
set autoscale
set output 'occurencesARN.png'
plot "occurencesARN.dat" using 1:2
set output 'occurencesARNKMP.png'
plot "occurencesARNKMP.dat" using 1:2
