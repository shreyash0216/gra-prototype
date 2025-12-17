from typing import List, Dict
import math

class SVGGenerator:
    """Generate SVG diagrams for farm layouts"""
    
    def __init__(self):
        self.width = 800
        self.height = 600
        self.colors = {
            "rice": "#4CAF50",
            "wheat": "#FFC107",
            "cotton": "#E91E63",
            "sugarcane": "#8BC34A",
            "soybean": "#FF9800",
            "maize": "#FFEB3B",
            "tomato": "#F44336",
            "onion": "#9C27B0",
            "millets": "#795548",
            "groundnut": "#607D8B",
            "water": "#2196F3",
            "infrastructure": "#9E9E9E"
        }
    
    def generate_farm_layout(self, farm_size: float, recommended_crops: List[str], 
                           water_source: str) -> str:
        """Generate SVG farm layout diagram"""
        
        # Calculate plot dimensions
        plots = self._calculate_plot_layout(farm_size, len(recommended_crops))
        
        # Start SVG
        svg_content = f'''<svg width="{self.width}" height="{self.height}" 
                         viewBox="0 0 {self.width} {self.height}" 
                         xmlns="http://www.w3.org/2000/svg">
        
        <!-- Background -->
        <rect width="{self.width}" height="{self.height}" fill="#f5f5f5" stroke="#ddd"/>
        
        <!-- Title -->
        <text x="{self.width//2}" y="30" text-anchor="middle" 
              font-family="Arial, sans-serif" font-size="20" font-weight="bold" fill="#333">
            Farm Layout Plan ({farm_size} acres)
        </text>
        '''
        
        # Add crop plots
        svg_content += self._add_crop_plots(plots, recommended_crops)
        
        # Add water source
        svg_content += self._add_water_source(water_source)
        
        # Add infrastructure
        svg_content += self._add_infrastructure()
        
        # Add legend
        svg_content += self._add_legend(recommended_crops)
        
        # Close SVG
        svg_content += "</svg>"
        
        return svg_content
    
    def _calculate_plot_layout(self, farm_size: float, num_crops: int) -> List[Dict]:
        """Calculate optimal plot layout"""
        plots = []
        
        # Available area for plots (excluding margins and infrastructure)
        plot_area_width = self.width - 200  # Leave space for legend and margins
        plot_area_height = self.height - 150  # Leave space for title and infrastructure
        
        # Calculate grid dimensions
        cols = math.ceil(math.sqrt(num_crops))
        rows = math.ceil(num_crops / cols)
        
        plot_width = plot_area_width // cols
        plot_height = plot_area_height // rows
        
        # Generate plot coordinates
        for i in range(num_crops):
            row = i // cols
            col = i % cols
            
            x = 50 + col * plot_width
            y = 60 + row * plot_height
            
            plots.append({
                "x": x,
                "y": y,
                "width": plot_width - 10,  # Add spacing between plots
                "height": plot_height - 10,
                "area": farm_size / num_crops  # Equal distribution for simplicity
            })
        
        return plots
    
    def _add_crop_plots(self, plots: List[Dict], crops: List[str]) -> str:
        """Add crop plots to SVG"""
        svg_content = ""
        
        for i, (plot, crop) in enumerate(zip(plots, crops)):
            color = self.colors.get(crop.lower(), "#4CAF50")
            
            # Plot rectangle
            svg_content += f'''
            <rect x="{plot['x']}" y="{plot['y']}" 
                  width="{plot['width']}" height="{plot['height']}" 
                  fill="{color}" stroke="#333" stroke-width="2" opacity="0.8"/>
            
            <!-- Crop label -->
            <text x="{plot['x'] + plot['width']//2}" y="{plot['y'] + plot['height']//2}" 
                  text-anchor="middle" font-family="Arial, sans-serif" 
                  font-size="14" font-weight="bold" fill="white">
                {crop.title()}
            </text>
            
            <!-- Area label -->
            <text x="{plot['x'] + plot['width']//2}" y="{plot['y'] + plot['height']//2 + 20}" 
                  text-anchor="middle" font-family="Arial, sans-serif" 
                  font-size="12" fill="white">
                {plot['area']:.1f} acres
            </text>
            '''
        
        return svg_content
    
    def _add_water_source(self, water_source: str) -> str:
        """Add water source representation"""
        svg_content = ""
        
        # Water source icon position
        x = self.width - 150
        y = self.height - 120
        
        if "bore" in water_source.lower() or "well" in water_source.lower():
            # Borewell/Well icon
            svg_content += f'''
            <circle cx="{x}" cy="{y}" r="25" fill="{self.colors['water']}" stroke="#333" stroke-width="2"/>
            <circle cx="{x}" cy="{y}" r="15" fill="white"/>
            <text x="{x}" y="{y + 5}" text-anchor="middle" font-family="Arial, sans-serif" 
                  font-size="12" font-weight="bold" fill="#333">W</text>
            <text x="{x}" y="{y + 45}" text-anchor="middle" font-family="Arial, sans-serif" 
                  font-size="10" fill="#333">Borewell</text>
            '''
        elif "river" in water_source.lower() or "canal" in water_source.lower():
            # River/Canal icon
            svg_content += f'''
            <path d="M {x-30} {y} Q {x-15} {y-10} {x} {y} Q {x+15} {y+10} {x+30} {y}" 
                  stroke="{self.colors['water']}" stroke-width="8" fill="none"/>
            <path d="M {x-30} {y+10} Q {x-15} {y} {x} {y+10} Q {x+15} {y+20} {x+30} {y+10}" 
                  stroke="{self.colors['water']}" stroke-width="6" fill="none"/>
            <text x="{x}" y="{y + 35}" text-anchor="middle" font-family="Arial, sans-serif" 
                  font-size="10" fill="#333">River/Canal</text>
            '''
        else:
            # Rainwater harvesting
            svg_content += f'''
            <rect x="{x-20}" y="{y-15}" width="40" height="30" 
                  fill="{self.colors['water']}" stroke="#333" stroke-width="2"/>
            <text x="{x}" y="{y + 5}" text-anchor="middle" font-family="Arial, sans-serif" 
                  font-size="12" font-weight="bold" fill="white">RWH</text>
            <text x="{x}" y="{y + 35}" text-anchor="middle" font-family="Arial, sans-serif" 
                  font-size="10" fill="#333">Rainwater</text>
            '''
        
        return svg_content
    
    def _add_infrastructure(self) -> str:
        """Add farm infrastructure elements"""
        svg_content = ""
        
        # Storage/Warehouse
        x = 50
        y = self.height - 80
        svg_content += f'''
        <rect x="{x}" y="{y}" width="60" height="40" 
              fill="{self.colors['infrastructure']}" stroke="#333" stroke-width="2"/>
        <text x="{x + 30}" y="{y + 25}" text-anchor="middle" font-family="Arial, sans-serif" 
              font-size="10" font-weight="bold" fill="white">Storage</text>
        '''
        
        # Farm house
        x = 150
        svg_content += f'''
        <rect x="{x}" y="{y}" width="50" height="40" 
              fill="#8D6E63" stroke="#333" stroke-width="2"/>
        <polygon points="{x},{y} {x+25},{y-15} {x+50},{y}" fill="#D32F2F"/>
        <text x="{x + 25}" y="{y + 55}" text-anchor="middle" font-family="Arial, sans-serif" 
              font-size="10" fill="#333">Farm House</text>
        '''
        
        return svg_content
    
    def _add_legend(self, crops: List[str]) -> str:
        """Add legend for crop colors"""
        svg_content = ""
        
        # Legend background
        legend_x = self.width - 180
        legend_y = 60
        legend_height = len(crops) * 25 + 40
        
        svg_content += f'''
        <rect x="{legend_x}" y="{legend_y}" width="160" height="{legend_height}" 
              fill="white" stroke="#333" stroke-width="1" opacity="0.9"/>
        <text x="{legend_x + 80}" y="{legend_y + 20}" text-anchor="middle" 
              font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#333">
            Crop Legend
        </text>
        '''
        
        # Legend items
        for i, crop in enumerate(crops):
            item_y = legend_y + 35 + i * 25
            color = self.colors.get(crop.lower(), "#4CAF50")
            
            svg_content += f'''
            <rect x="{legend_x + 10}" y="{item_y}" width="20" height="15" 
                  fill="{color}" stroke="#333" stroke-width="1"/>
            <text x="{legend_x + 40}" y="{item_y + 12}" font-family="Arial, sans-serif" 
                  font-size="12" fill="#333">{crop.title()}</text>
            '''
        
        return svg_content