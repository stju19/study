import com.sun.istack.internal.NotNull

object Hello extends App {
  val a= new A
  println(a)
  println(a.foo)
}

class A {
  def foo() = this
}