### Data Innovation Solution

Project to harness tide data to provide real time soil safety risk.

Challenge:

Mapping Data for Societal Benefit

The world is facing many big challenges like climate change, water insecurity, and diseases; addressing these challenges in innovative ways requires interdisciplinary research using data from multiple sources. Many U.S. government agencies have substantial archives of high-quality, freely available data, but these archives can be difficult to navigate. Your challenge is to design a platform to explore open data that is available from NASA and other federal data repositories or to improve the functionality of an existing such platform, and then demonstrate how your solution can be applied to an area of study that has significant societal benefits (e.g., environmental justice, ecological conservation, or human health).
Problem:
The problem we're addressing is the difficulty in accessing and analyzing vital data from NASA and other sources, hindering our ability to understand and tackle environmental challenges. The existing data platform is not user-friendly and requires improvement. Additionally, there's a pressing need for accurate measurements of water mineral quality for agriculture. Climate change is causing saltwater intrusion into tributaries and estuaries, which can lead to reduced crop yields with significant societal consequences. Our solution aims to provide easier access to data, enhance measurement accuracy, and better prepare for such environmental changes, using the 'Bay of Fundy' as an example.
High level overview:
We've developed an innovative platform called Data Innovative solutions that simplifies access to critical NASA and federal data, coupled with hardware and potentially adding AI-driven insights. This solution addresses the challenge of data accessibility and accuracy, empowering users to tackle environmental challenges, optimize agriculture, prepare for climate changes amongst other potential uses. The project is important because it enables data-driven decision-making, promoting sustainability, and contributing to a better informed future for our planet.

Solution:

We've developed a user-friendly platform that simplifies access to NASA and federal data while improving data accuracy through hardware and mobile apps. This platform benefits agriculture by assessing water mineral quality and aiding crop selection with AI predictions. Additionally, it enhances environmental modeling by incorporating real-time measurements and user contributions for better preparation against climate-induced challenges. like saltwater intrusion in areas like the 'Bay of Fundy.'

Value proposition:
Our solution simplifies access to critical NASA and federal data by offering a user-friendly platform with advanced analysis tools and collaboration features. We provide a mobile app and precise hardware for accurate measurements, particularly in agriculture, aiding soil quality assessment. With AI-driven insights, we empower farmers to make informed decisions on crop selection for each season, enhancing agricultural productivity.

Vision 

Use the power of data for a sustainable future, our vision is to create a world where open data is easily accessible and empowers individuals, researchers, and organizations to address pressing environmental challenges with confidence and precision.

Mission

Provide an innovative platform that simplifies access to NASA and federal data, enhancing its utility through user-friendly interfaces, advanced analysis tools, and collaborative features. We aim to enable more informed decision-making in agriculture, environmental conservation, and beyond, improving the quality of life and the health of our planet.

Our Project is aimed at improving the functionality of an existing platform by using databases for C-Band SAR, Tidal Data, Lunar Data, AMOC and Echo Scouter Data. Our solution will improve user interface and functionality, offer access to NASA and federal data archives, advanced analysis tools and collaborative research capabilities. 

The solution includes a Mobile app for facilitating user interface, hardware for analyzing improved reproducibility and reliability. In the agriculture sector this helps determine the quality of the minerals in the water which get washed ashore which would make for good quality soil. With additional training AI sets we could have better predictions of the area, the soil and what type of crop would be best to farm for that timeframe/season.  By comparing  which includes silt, magnesium, iron, phosphate, iron. The hardware is provided by Stella, an open source hardware which utilizes Bluefruit connect for visual representation of data. 

Spectral data has environmental variables such as:
Cloud Cover
Humidity
Temperature 

Stella’s hardware and measurements provide 1 reliable point which is based on optical density. This reads silt and other minerals like magnesium, nitrate, phosphate which in higher quantities provide better nutrients for the soil. 

As for the STELLA 1.1 it is a device that allows us to measure. It has sensors to detect different types of light, pressure, humidity, temperature, and more. The data collected can include things like the time, date, and location. This device can help us gather information about the world around us.
The cool thing is that this device can be improved to work with phones like iPhones and Androids. It can even measure things like how fast it's moving and which way it's pointing. This is really useful when we want to know more about our surroundings.
By using this device, we can collect very accurate information. For example, we can make measurements that are as precise as possible by comparing them to known standards. Imagine mixing different amounts of a liquid and measuring how much light it absorbs. This helps us know exactly what we're looking at.
One interesting place where this device is useful is the Bay of Fundy because it's quite shallow. When we use special radar technology there, we can measure things beneath the water's surface. This helps us get even more data to understand our environment better.
In simple terms, STELLA 1.1 is a tool that helps us collect important information about our world, and it can become even more powerful in the future. We use it to measure things accurately and learn more about the environment, especially in places like the Bay of Fundy.

Software:

Django with Python - We employed Python in conjunction with the Django framework to efficiently process data from the NOAA website (tidesandcurrents.noaa.gov). This data was seamlessly integrated into our platform, allowing us to generate predictive visualizations that enhance the functionality and usefulness of our solution.

Hardware:

Assembly of the STELLA 1.1

The STELLA prototype was built off of the frameworks previously established. The electronic board contains (1) a Near Infrared Spectral Sensor (2) a Visible Light Spectral Sensor (3) a Pressure and Humidity Sensor (4) a MicroSD Card (5) a Display Screen (6) a Rechargeable Battery (7) a Temperature Sensor. 

The platform is built off of the Adafruit Featherboard (Adafruit Feather RP2040) with an expansion for datalogging to an Adalogger Featherwing (Adalogger FeatherWing ID:2922). Spectral wavelengths that can be collected include both Visible Spectral Bands (B500, G550, Y570, O600, R650) and Near Infrared Spectral Bands (610, 680, 730, 760, 810, 860). Each datapoint is compared against the existing conditions of (1) air temperature (2) surface temperature (3) the time (UTC) and (4) date. For each data point supplemental resources would include a GPS coordinate to be reported with each measurement.

Under ideal conditions the platform would be expanded to be compatible with the STELLA 2.0 platform which interfaces directly with both iPhone and Android devices through the Bluefruit Connect App. Expanded capability includes accelerometers, gyroscopes, and magnetometers and the ability to report GPS coordinates with each data point.

Calibration Standards and Improvements

Using the expansion of the STELLA platform it is possible to use a fixed path-length with a cuvette. This allows for substantially better quality of data because of the capacity for: collecting blank measurements, using fixed path lengths, using fixed spectral bands, creating calibration curves and using colorimetric indicators. 

In collecting a calibration standard we can collect high quality data-sets. For instance, if we set a calibration standards of a serial dilution comprised of: 1:2, 1:10, 1:20, and 1:100 dilutions against a fixed path length. In doing so we can collect repeat data points and assign confidence intervals to each measurement with greater precision. For instance, the BCA (or Bichinoic Acid) assay (https://www.caymanchem.com/product/701780/protein-determination-(bca)-kit) is a standard of use in the biotech community that collects standards in units of uG/mL against absorbance at 560 nM. From this accurate, timestamped measurements can be collected and aggregated and compared against existing frameworks.


Among other experimental measurements that can be collected include (1) phosphate measurements (Malachite Green Assay) with ABS at 620 nM (2) nitrate concentrations (Greiss Reagent) with ABS at 540 nM.

What is geographically unique about the region of the ‘Bay of Fundy’ is that it is a shallow depth. This shallow depth can be analogous to a fixed focal path length for more reproducible measurements 


Excerpt From: Mapping seafloor habitats in the Bay of Fundy to assess megafaunal assemblages associated with Modiolus modiolus beds Brittany R. Wilson a,b,*,1 , Craig J. Brown d , Jessica A. Sameoto c , Myriam Lacharit´e e , Anna M. Redden b , Vicki Gazzola

In particular the regions of the Minas Basin, Chignecto Bay, and the Qoddy Regions are especially shallow allowing for shallow penetrating spectral measurements from satellite data sets. Of particular interest is the use of SAR or synthetic Aperture Radar which is comprised of the Radio to Microwave Frequency region. While the SAR technique has a limited depth of penetration by coordinating with receding tides gives an overabundance of silt for spectral measurements. When coordinated against the measurements collected from the STELLA spectrometer the reliability of data is improved upon.



Excerpt from: Mapping seafloor habitats in the Bay of Fundy to assess megafaunal assemblages associated with Modiolus modiolus beds Brittany R. Wilson a,b,*,1 , Craig J. Brown d , Jessica A. Sameoto c , Myriam Lacharit´e e , Anna M. Redden b , Vicki Gazzola


While SAR has a limited depth of penetration 





Wavelength bands for SAR are divided into Band Frequencies against the microwave and radio frequency spectra. 

BEERS LAW



Absorbance = Molar absorptivity * path length * and concentration 
