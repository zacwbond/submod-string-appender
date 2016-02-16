
print("BROKEN")
exit(1)

def append_abc(s):
  return 'abc_' + s
  
def append_bcd(s):
  return 'bcd_' + s
  
def append_efg(s):
  return 'efg_' + s
  
def append_stinker(s):
  return 'eww_' + s  


if __name__ == '__main__':
  def unit_test(f, s, expected):
    if f(s) != expected:
      return False
    return True
  
  tests = { 
    'hello abc': (append_abc, 'hello world', 'abc_hello world'),
    'hello bcd': (append_bcd, 'hello world', 'bcd_hello world')
  }
  
  print("\n\nPerforming the world's most incompetent unit test...")
  results = [(t, unit_test(f, s, e)) for (t, (f, s, e)) in tests.items()]    
  if all(results):
    print('\n\nALL TESTS PASSED!')
  else:
    print('\n'.join([t + ' test FAILED' for (t, p) in results if not p]))
      
  
