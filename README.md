# RealitySports

Team Quasar.

A platform leveraging advanced deep learning techniques to create highly realistic 3D sports environments using any camera.

# Inspiration

Sports have been 2D for 84 years! Our most iconic moments are captured around the world – why not view them in 3D for a more immersive experience? 3D technology might enable the future of realistic sports environments, right at home. Moreover, 3D scenes may enable advanced coaching and officiating opportunities. At Hacklytics, Team Quasar used advanced deep learning techniques to enable never-before seen 3D experiences in athletics.

# What it does

Reality Sports accelerates the creation of highly realistic virtual worlds which can be produced easily with any camera. We demonstrate that recent advances in artificial intelligence enable high-quality scene mapping and exploration, with easy-to-use hardware. 

# How we built it

During the weekend, Team Quasar procured and analyzed a highly custom dataset at the Georgia Tech Campus Recreational Center (CRC) using a LiDAR sensors on our mobile devices. LiDAR fields were processed using custom Python code and analyzed using NeRF models. NeRF implementation was enabled through the open-source NVidia Instant-NGP software (https://github.com/NVlabs/instant-ngp). 

Camera scenes were programmed for showing off our custom NeRF scenes! Furthermore, NeRF analysis enabled output of high-quality 3D meshes, allowing us to further augment traditional sports content in an interactive, creative fashion. 

# Challenges we ran into

Key technical challenges we faced included limited compute capabilities during the weekend. While being limited to a single Nvidia GeForce RTX 3060, we struggled with loading some of the largest NeRF models and were forced to limit our dataset size. We believe that increased compute availability may help increase the quality of our NeRFs with additional dataset size. Furthermore, while we did integrate VR capabilities with our NeRF solution, we were unable to produce high-quality VR experiences due to framerate and compute limitations. 

# Accomplishments that we're proud of

We are proud to have created highly scalable and accessible pipeline to represent sports moments in 3D. Furthermore, we got to experiment with interactive high-fidelity augmented experiences which can be extended to custom virtual realities. It was our first time using the NeRF technology, and we are very proud to deliver a product which has endless applications including instant replay reviews, film studies for teams and coaches, and immersive VR for all spectators around the world.

# What we learned

We gained much experience using Python for image processing, including popular packages such as Pillow and OpenCV. We gained experience with super resolution techniques for data augmentation, including ESRGAN. Furthermore, we gained insights on the complexities of creating high-quality NeRFs and walk away with a better understanding of the requirements for taking NeRFs to production. 

# What's next for Reality Sports

With more time, Reality Sports hopes to further improve NeRF creation capabilities. We aspire to film a live sports game and evaluate the use of NeRFs for evolving a virtual experience in real-time. Furthermore, we hope to render these events in VR.  

# Built With
•	Neural Radiance Fields (NeRFs)
•	Python: NumPy, OpenCV, Pillow
•	LiDAR: Record3D (iOS App)
•	Docker: Virtualization
•	Blender: Rendering
•	MeshLab: Mesh optimization and refinement


# About us:
1. Aniket Pant: 3rd year BS MSE @ GT. Passionate about scientific machine learning.
2. Ritvik Verma: 2nd year BS CompE @ GT. Passionate about cybersecurity and multimedia creation.
3. Abhinav Gullapalli: 1st year MS CS @ GT. Passionate about machine learning and natural language processing. 
