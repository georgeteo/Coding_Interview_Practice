/* 
 	CCC 1.4: CCC 1.4: Given a string, replace spaces with %20.
*/

def replace_solution(s: String): String = {
	s.replaceAll("\\s", "%20")
}

println(replace_solution("a b  c"))