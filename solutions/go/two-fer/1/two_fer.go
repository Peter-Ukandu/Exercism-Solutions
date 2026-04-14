package twofer

import "fmt"

// ShareWith should have a comment documenting it.
func ShareWith(name string) (msg string) {
	if name == ""  {
    	name = "you"
    }
    msg = fmt.Sprintf("One for %v, one for me.", name)
	return
}
