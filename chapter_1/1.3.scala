/* 
 	CCC 1.3: Given two strings, check whether they are 
 	         permutations of each other.
*/

def map_solution(s: String, t: String): Boolean = {
	true
}

def sort_solution(s: String, t: String): Boolean = {
	s.toList.sorted == t.toList.sorted
}

println(sort_solution("abbc","babc"))
println(sort_solution("abbc","abcd"))