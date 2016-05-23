func fibonacci(number: Int) -> (Int){
     var n1 = 0
     var n2 = 1
     for _ in 0..<number{
     	 let temp=n1
	 n1=n2
	 n2=temp+n1
     }
     return n1
}