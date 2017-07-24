#set java environment
export JAVA_HOME=/usr/java/jdk1.7.0_79
export JRE_HOME=$JAVA_HOME/jre
export PATH=${JAVA_HOME}/bin:$JAVA_HOME/jre/bin:$PATH
export CLASSPATH=$CLASSPATH:.:$JAVA_HOME/lib:$JAVA_HOME/jre/lib

#set scala home
export SCALA_HOME=/usr/local/scala-2.10.4
export PATH=$SCALA_HOME/bin:$PATH

#set gradle home
export GRADLE_HOME=/usr/local/gradle-1.11
export PATH=$GRADLE_HOME/bin:$PATH