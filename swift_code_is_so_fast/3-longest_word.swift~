func longest_word(text: String) -> (String){
     let splitted :[String] = text.characters.split{$0 == " "}.map(String.init)
     if let max = splitted.maxElement({$1.characters.count > $0.characters.count}){
     	return max
     }
     return ""
}