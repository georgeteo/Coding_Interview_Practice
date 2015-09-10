/* 
 	CCC 1.1: Implement an algorithm to determine if a string
 	         gas all unique characters
*/

def wrong_solution(s: String): Boolean = {
	s.length == s.length
}

def set_solution(s: String): Boolean = {
	s.toSet.size == s.size
}



println(set_solution("abcd1234"))
println(set_solution("abcd1234a"))
println(set_solution("abcd1234A"))