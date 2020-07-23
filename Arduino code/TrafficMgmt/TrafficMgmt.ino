
int lane1_1 =2;
int lane1_2 =3;
int lane1_3 =4;

int lane2_1 =5;
int lane2_2 =6;
int lane2_3 =7;

int lane3_1 =8;
int lane3_2 =9;
int lane3_3 =10;

int lane4_1 =11;
int lane4_2 =12;
int lane4_3 =13;

int curLit =0;

void setup() {
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
 
  pinMode(lane1_1 , OUTPUT);
  pinMode(lane1_2 , OUTPUT);
  pinMode(lane1_3 , OUTPUT);
  pinMode(lane2_1 , OUTPUT);
  pinMode(lane2_2 , OUTPUT);
  pinMode(lane2_3 , OUTPUT);
  pinMode(lane3_1 , OUTPUT);
  pinMode(lane3_2 , OUTPUT);
  pinMode(lane3_3 , OUTPUT);
  pinMode(lane4_1 , OUTPUT);
  pinMode(lane4_2 , OUTPUT);
  pinMode(lane4_3 , OUTPUT);
}

void loop() {

  char data;
  while (Serial.available()){
  data = Serial.read();
  }
  
  if (data == '0')
 {
  digitalWrite (curLit*3, HIGH);
  digitalWrite (curLit*3-1 , LOW);
  digitalWrite (curLit*3+1 , LOW);
}
  else if (data == '1')
 {
  curLit = 1;
  digitalWrite (lane1_1, LOW);
  digitalWrite (lane1_2, LOW);
  digitalWrite (lane1_3, HIGH);

  digitalWrite (lane2_1, HIGH);
  digitalWrite (lane2_2, LOW);
  digitalWrite (lane2_3, LOW);
  
  digitalWrite (lane3_1, HIGH);
  digitalWrite (lane3_2, LOW);
  digitalWrite (lane3_3, LOW);

  digitalWrite (lane4_1, HIGH);
  digitalWrite (lane4_2, LOW);
  digitalWrite (lane4_3, LOW);
}
  else if (data == '2')
 {
  curLit = 2;
  digitalWrite (lane1_1, HIGH);
  digitalWrite (lane1_2, LOW);
  digitalWrite (lane1_3, LOW);

  digitalWrite (lane2_1, LOW);
  digitalWrite (lane2_2, LOW);
  digitalWrite (lane2_3, HIGH);
  
  digitalWrite (lane3_1, HIGH);
  digitalWrite (lane3_2, LOW);
  digitalWrite (lane3_3, LOW);

  digitalWrite (lane4_1, HIGH);
  digitalWrite (lane4_2, LOW);
  digitalWrite (lane4_3, LOW);
}
  else if (data == '3')
 {
  curLit = 3;
  digitalWrite (lane1_1, HIGH);
  digitalWrite (lane1_2, LOW);
  digitalWrite (lane1_3, LOW);

  digitalWrite (lane2_1, HIGH);
  digitalWrite (lane2_2, LOW);
  digitalWrite (lane2_3, LOW);
  
  digitalWrite (lane3_1, LOW);
  digitalWrite (lane3_2, LOW);
  digitalWrite (lane3_3, HIGH);

  digitalWrite (lane4_1, HIGH);
  digitalWrite (lane4_2, LOW);
  digitalWrite (lane4_3, LOW);
}
  else if (data == '4')
  {
  curLit = 4;
  
  digitalWrite (lane1_1, HIGH);
  digitalWrite (lane1_2, LOW);
  digitalWrite (lane1_3, LOW);

  digitalWrite (lane2_1, HIGH);
  digitalWrite (lane2_2, LOW);
  digitalWrite (lane2_3, LOW);
  
  digitalWrite (lane3_1, HIGH);
  digitalWrite (lane3_2, LOW);
  digitalWrite (lane3_3, LOW);

  digitalWrite (lane4_1, LOW);
  digitalWrite (lane4_2, LOW);
  digitalWrite (lane4_3, HIGH);
  }
}
 


  
  
}
