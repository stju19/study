//object test extends App{
////  var log = new Logger with Base with A with B with C
////  log
////    .log()
////  println(函数())
//
//  var Frac(a,1)=new Frac(123)
//  println(a)
//
//  class Frac(x:Int){
//    var a = x
//  }
//
//  object Frac{
//    def apply(x:Int) = new Frac(x+1)
//    def unapply(a:Frac) = Some(a.a, 1)
//  }
//
//  def 函数() = 1
//
//  class Time(var hours:Int, private var minutes:Int) {
//    def before(other:Time) = {
//      hours < other.hours || (hours == other.hours && minutes < other.minutes)
//    }
//  }
//
//  trait Base{
//    def log(){}
//  }
//  trait A extends Base{
//    override def log(){
//      println("A")
//      super.log()
//    }
//  }
//
//  trait B extends Base{
//    override def log(){
//      println("B")
//      super.log()
//    }
//  }
//
//  trait C extends Base{
//    override def log(){
//      println("C")
//      super.log()
//    }
//  }
//
//  trait ConcoleLogger {
//    def log(msg:String) {println(msg)}
//  }
//
//  class Logger{}
//}

object Hello {
  def main (args: Array[String]) {
    println("Hello World!")
  }
}