func factorial(N: Int) -> (Int){
     var fact :Int = 1
     for i in 1...N{
     	 fact*=i
     }
     return fact
}