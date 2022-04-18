from typing import List
from typing import Optional

def lower_join(seq: List[Optional[str]]) -> str:
    
    """Принимает на вход последовательность и создаёт из неё  
    строку в нижнем регистре."""
    
    return ''.join(seq).lower()

hoku: List[Optional[str]] = ['16:00. ', 'Быстро пустеет парковка. ', 'Пятница']
empty: List[Optional[str]] = []

print (lower_join(hoku))
print (lower_join(empty))