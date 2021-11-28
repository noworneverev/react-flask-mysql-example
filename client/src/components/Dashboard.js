import * as React from "react";
import { Card, CardContent, CardHeader } from "@material-ui/core";
// import { ComposableMap, Geographies, Geography } from "react-simple-maps";

import MapChart from "./MapChart";

// const geoUrl =
//   "https://raw.githubusercontent.com/zcreativelabs/react-simple-maps/master/topojson-maps/world-110m.json";

const Dashboard = () => (
  <div>
    <Card>
      <CardHeader title="Welcome to the administration" />
      <CardContent>Lorem ipsum sic dolor amet...</CardContent>
    </Card>

    <MapChart />
    {/* <ComposableMap>
      <Geographies geography={geoUrl}>
        {({ geographies }) =>
          geographies.map((geo) => (
            <Geography key={geo.rsmKey} geography={geo} />
          ))
        }
      </Geographies>
    </ComposableMap> */}
  </div>
);

export default Dashboard;
