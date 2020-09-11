from model import Model

model = Model('model')

context = """

Augustus, also called Augustus Caesar or (until 27 BCE) Octavian, original name Gaius Octavius, adopted name Gaius Julius Caesar Octavianus, (born September 23, 63 BCE—died August 19, 14 CE, Nola, near Naples [Italy]), first Roman emperor, following the republic, which had been finally destroyed by the dictatorship of Julius Caesar, his great-uncle and adoptive father. His autocratic regime is known as the principate because he was the princeps, the first citizen, at the head of that array of outwardly revived republican institutions that alone made his autocracy palatable. With unlimited patience, skill, and efficiency, he overhauled every aspect of Roman life and brought durable peace and prosperity to the Greco-Roman world.

"""
question = "Who is Augustus"

answer = model.predict(context, question)

print("Question: " + question)
print("Answer: " + answer["answer"])
