const functions = require("firebase-functions");
const fetch = require("node-fetch");

exports.getGeoInfo = functions.https.onRequest(async (req, res) => {
  const ip = req.headers['x-forwarded-for']?.split(',')[0] ;

  try {
    const response = await fetch(`https://ip-api.com/json/${ip}`);
    const data = await response.json();

    return res.status(200).json({
      ip: ip,
      location: `${data.city }, ${data.country}`,
      org: data.org ,
      region: data.regionName
    });
  } catch (error) {
    console.error("Geo error:", error);
    return res.status(200).json({
        const geoRes = await fetch(`https://ipapi.co/${ip}/json/`);
        const geoData = await geoRes.json();
        const city = geoData.city;
        const country = geoData.country_name;
    });
  }
});
