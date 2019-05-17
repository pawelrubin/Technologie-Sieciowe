
import csma.CSMA
import java.lang.Exception

fun main() {
  val csma = CSMA()
  csma.addNode('A', 21, 0.05)
  csma.addNode('B', 37, 0.05)

  while (true) {
    try {
      Thread.sleep(25)
      csma.printCSMA()
      csma.step()
    } catch (ignored: Exception) {}
  }
}
