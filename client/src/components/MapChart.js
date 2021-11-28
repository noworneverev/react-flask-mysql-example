import React from "react";
import { useHistory } from "react-router-dom";
import {
  ComposableMap,
  Geographies,
  Geography,
  Graticule,
} from "react-simple-maps";

const geoUrl =
  "https://raw.githubusercontent.com/zcreativelabs/react-simple-maps/master/topojson-maps/world-110m.json";

const MapChart = () => {
  const history = useHistory();

  const routeChange = (name) => {
    // let path = `newPath`;
    // let path = `users?displayedFilters=%7B%7D&filter=${"mike"}&order=ASC&page=1&perPage=10&sort=id`;
    let path = `users?displayedFilters=%7B%7D&filter=%7B%22q%22%3A%22${name}%22%7D&order=ASC&page=1&perPage=10&sort=id`;
    history.push(path);
  };

  return (
    <ComposableMap projectionConfig={{ scale: 147 }}>
      <Graticule stroke="#F53" />
      <Geographies geography={geoUrl}>
        {({ geographies }) =>
          geographies.map((geo) => (
            <Geography
              onClick={() => routeChange(geo.properties.NAME)}
              key={geo.rsmKey}
              geography={geo}
            />
          ))
        }
      </Geographies>
    </ComposableMap>
  );
};

export default MapChart;
