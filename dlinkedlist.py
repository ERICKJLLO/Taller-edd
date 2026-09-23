from types import new_class
import random
class NodeD:

  __slots__ = ("__value","__next", "__prev")

  def __init__(self,value):
    self.__value = value
    self.__next = None
    self.__prev = None

  @property
  def value(self):
    return self.__value

  @property
  def next(self):
    return self.__next

  @property
  def prev(self):
    return self.__prev

  @value.setter
  def value(self, new_value):
    if new_value is None:
      raise TypeError("El valor No debe ser None/Null.")
    self.__value = new_value

  @next.setter
  def next(self, new_next):
    if new_next is not None and not isinstance(new_next,NodeD):
      raise TypeError("El next de un nodo, solo puede ser None ó otro Nodo")
    self.__next = new_next


  @prev.setter
  def prev(self, new_prev):
    if new_prev is not None and not isinstance(new_prev,NodeD):
      raise TypeError("El prev de un nodo, solo puede ser None ó otro Nodo")
    self.__prev = new_prev



  def __str__(self):
    return str(self.__value)


class dlinkedlist:

  __slots__ = ("__head","__tail","__size")

  def __init__(self):
    self.__head = None
    self.__tail = None
    self.__size = 0

  @property
  def head(self):
    return self.__head

  @property
  def tail(self):
    return self.__tail

  @property
  def size(self):
    return self.__size

  @head.setter
  def head(self, new_head):
    if new_head is not None and not isinstance(new_head,NodeD):
      raise TypeError("La cabeza de una lista enlazada, solo puede ser None ó otro Nodo")
    self.__head = new_head

  @tail.setter
  def tail(self, new_tail):
    if new_tail is not None and not isinstance(new_tail,NodeD):
      raise TypeError("La cola de una lista enlazada, solo puede ser None ó otro Nodo")
    self.__tail = new_tail

  @size.setter
  def size(self, new_size):
    if not isinstance(new_size,int):
      raise TypeError("El tamaño de una lista enlazada, solo puede ser un numero entero")
    self.__size = new_size

  def __iter__(self):
    cur_node = self.__head
    while cur_node is not None:
      yield cur_node
      cur_node = cur_node.next

  def __str__(self):
     result = [str(node.value) for node in self]
     return ' <--> '.join(result)

  def prepend(self, value):

    new_node = NodeD(value)
    if self.__head is None:
      self.__tail = new_node
    else:
      self.head.prev = new_node

    new_node.next = self.__head
    self.__head = new_node
    self.__size += 1


  def append(self, value):
    new_node = NodeD(value)

    if self.__tail is None:
      self.__head = new_node
    else:
      self.__tail.next = new_node
      new_node.prev = self.__tail

    self.__tail = new_node
    self.__size += 1

  def getvaluebyindex(self,index):

    if not isinstance(index,int) or (index>self.__size-1) or (index <-1) :
      raise ValueError("Indice por fuera de rango ó no es tipo entero")

    if index == 0:
      return self.__head.value
    elif index == -1 or index == self.__size-1:
      return self.__tail.value
    else:
      i_temp = 0
      for cur_node in self:
        if i_temp == index:
          return cur_node.value
        i_temp += 1

  def getnodebyindex(self,index):

    if not isinstance(index,int) or (index>self.__size-1) or (index <-1) :
      raise ValueError("Indice por fuera de rango ó no es tipo entero")

    if index == 0:
      return self.__head
    elif index == -1 or index == self.__size-1:
      return self.__tail
    else:
      i_temp = 0
      for cur_node in self:
        if i_temp == index:
          return cur_node
        i_temp += 1


  def insertvaluebyindex(self,index,new_value):

    if not isinstance(index,int) or (index>self.__size) or (index <-1) :
      raise ValueError("Indice por fuera de rango ó no es tipo entero")

    if index == 0:
      self.prepend(new_value)
    elif index == -1 or index == self.__size:
      self.append(new_value)
    else:
      new_node = NodeD(new_value)
      prev_node = self.getnodebyindex(index-1)
      next_node = prev_node.next
      print("prev_node :", prev_node)
      new_node.next = next_node
      next_node.prev = new_node #previo del nodo siguiente

      new_node.prev = prev_node #previo del nuevo nodo
      prev_node.next = new_node
      self.__size += 1


  def searchvalue(self,value_to_find):

    for cur_node in self:
      if cur_node.value == value_to_find:
          return True
    return False

  def setnewvalue(self,value_to_find, new_value):

    for cur_node in self:
      if cur_node.value == value_to_find:
        cur_node.value = new_value
        return True
    return False


  def popfirst(self):

    temp_node = self.head

    if self.__head is None:
      raise TypeError("La lista esta vacía no hay elementos a eliminar")
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
    else:
      self.__head = self.__head.next
      self.__head.prev = None #elimino el previo, es decir la cabeza original
    self.__size -= 1

    temp_node.next = None
    temp_node.prev = None
    return temp_node


  def pop(self):

    temp_node = self.tail

    if self.__head is None:
      raise TypeError("La lista esta vacía no hay elementos a eliminar")
    elif self.__size == 1:
      self.__head = None
      self.__tail = None
    else:
      prev_tail = self.__tail.prev
      print("prev_tail",prev_tail)

      prev_tail.next = None
      self.__tail = prev_tail

    self.__size -= 1

    temp_node.prev = None
    return temp_node

  def generate(self, num, min, max):
    for _ in range(num):
      self.append(random.randint(min,max))