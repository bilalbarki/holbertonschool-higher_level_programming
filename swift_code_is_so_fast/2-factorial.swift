func factorial(N: Int) -> (Int){
     if N==0{
     	return 1
     }
     var fact :Int = 1
     for i in 1...N{
     	 fact*=i
     }
     return fact
}