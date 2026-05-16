#!/usr/bin/env python3
"""
Data Validation Script for PathPilot AI
Validates all data files for completeness and correctness.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any
from urllib.parse import urlparse


def load_json(filepath: Path) -> Any:
    """Load and parse a JSON file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[FAIL] File not found: {filepath}")
        return None
    except json.JSONDecodeError as e:
        print(f"[FAIL] Invalid JSON in {filepath}: {e}")
        return None


def validate_url(url: str) -> bool:
    """Check if URL has valid format"""
    if not url or url in ['#', '', 'https://example.com']:
        return False
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False


def validate_projects(data_dir: Path) -> bool:
    """Validate projects.json"""
    print("\n" + "=" * 80)
    print("VALIDATING projects.json")
    print("=" * 80)
    
    filepath = data_dir / 'projects.json'
    data = load_json(filepath)
    if data is None:
        return False
    
    if not isinstance(data, list):
        print(f"[FAIL] Expected list, got {type(data)}")
        return False
    
    issues = []
    for i, skill_group in enumerate(data):
        if 'skill' not in skill_group:
            issues.append(f"Item {i}: Missing 'skill' field")
        if 'projects' not in skill_group:
            issues.append(f"Item {i}: Missing 'projects' field")
        else:
            projects = skill_group['projects']
            if not isinstance(projects, list):
                issues.append(f"Item {i}: 'projects' should be a list")
            else:
                for j, project in enumerate(projects):
                    if 'title' not in project:
                        issues.append(f"Item {i}, Project {j}: Missing 'title'")
                    if 'description' not in project:
                        issues.append(f"Item {i}, Project {j}: Missing 'description'")
                    if 'difficulty' not in project:
                        issues.append(f"Item {i}, Project {j}: Missing 'difficulty'")
    
    if issues:
        print(f"[FAIL] Found {len(issues)} issues:")
        for issue in issues[:10]:  # Show first 10
            print(f"   - {issue}")
        return False
    
    print(f"[PASS] Valid: {len(data)} skill groups with projects")
    return True


def validate_verified_projects(data_dir: Path) -> bool:
    """Validate verified_projects.json"""
    print("\n" + "=" * 80)
    print("VALIDATING verified_projects.json")
    print("=" * 80)
    
    filepath = data_dir / 'verified_projects.json'
    data = load_json(filepath)
    if data is None:
        return False
    
    if not isinstance(data, dict):
        print(f"[FAIL] Expected dict, got {type(data)}")
        return False
    
    required_careers = [
        'data_analyst', 'soc_analyst', 'software_developer',
        'cloud_engineer', 'it_help_desk', 'web_developer',
        'cybersecurity', 'ai_ml_engineer', 'general'
    ]
    
    issues = []
    invalid_urls = []
    
    for career in required_careers:
        if career not in data:
            issues.append(f"Missing career path: {career}")
        else:
            projects = data[career]
            if not isinstance(projects, list):
                issues.append(f"{career}: Expected list of projects")
            else:
                for i, project in enumerate(projects):
                    if 'title' not in project:
                        issues.append(f"{career}[{i}]: Missing 'title'")
                    if 'url' not in project:
                        issues.append(f"{career}[{i}]: Missing 'url'")
                    elif not validate_url(project['url']):
                        invalid_urls.append(f"{career}[{i}]: Invalid URL: {project.get('url')}")
                    if 'difficulty' not in project:
                        issues.append(f"{career}[{i}]: Missing 'difficulty'")
                    if 'skills' not in project:
                        issues.append(f"{career}[{i}]: Missing 'skills'")
    
    if issues:
        print(f"[FAIL] Found {len(issues)} structural issues:")
        for issue in issues[:10]:
            print(f"   - {issue}")
    
    if invalid_urls:
        print(f"[WARN] Found {len(invalid_urls)} invalid URLs:")
        for issue in invalid_urls[:10]:
            print(f"   - {issue}")
    
    if not issues and not invalid_urls:
        total_projects = sum(len(projects) for projects in data.values())
        print(f"[PASS] Valid: {len(data)} career paths with {total_projects} total projects")
        return True
    
    return len(issues) == 0  # URLs can be invalid but structure must be correct


def validate_resources(data_dir: Path) -> bool:
    """Validate resources.json"""
    print("\n" + "=" * 80)
    print("VALIDATING resources.json")
    print("=" * 80)
    
    filepath = data_dir / 'resources.json'
    data = load_json(filepath)
    if data is None:
        return False
    
    if not isinstance(data, list):
        print(f"[FAIL] Expected list, got {type(data)}")
        return False
    
    issues = []
    invalid_urls = []
    
    for i, skill_group in enumerate(data):
        if 'skill' not in skill_group:
            issues.append(f"Item {i}: Missing 'skill' field")
        if 'resources' not in skill_group:
            issues.append(f"Item {i}: Missing 'resources' field")
        else:
            resources = skill_group['resources']
            if not isinstance(resources, list):
                issues.append(f"Item {i}: 'resources' should be a list")
            else:
                for j, resource in enumerate(resources):
                    if 'title' not in resource:
                        issues.append(f"Item {i}, Resource {j}: Missing 'title'")
                    if 'type' not in resource:
                        issues.append(f"Item {i}, Resource {j}: Missing 'type'")
                    if 'url' not in resource:
                        issues.append(f"Item {i}, Resource {j}: Missing 'url'")
                    elif not validate_url(resource['url']):
                        invalid_urls.append(f"Item {i}, Resource {j}: Invalid URL: {resource.get('url')}")
    
    if issues:
        print(f"[FAIL] Found {len(issues)} structural issues:")
        for issue in issues[:10]:
            print(f"   - {issue}")
    
    if invalid_urls:
        print(f"[WARN] Found {len(invalid_urls)} invalid URLs:")
        for issue in invalid_urls[:10]:
            print(f"   - {issue}")
    
    if not issues and not invalid_urls:
        total_resources = sum(len(sg['resources']) for sg in data if 'resources' in sg)
        print(f"[PASS] Valid: {len(data)} skill groups with {total_resources} total resources")
        return True
    
    return len(issues) == 0


def validate_verified_resources(data_dir: Path) -> bool:
    """Validate verified_resources.json"""
    print("\n" + "=" * 80)
    print("VALIDATING verified_resources.json")
    print("=" * 80)
    
    filepath = data_dir / 'verified_resources.json'
    data = load_json(filepath)
    if data is None:
        return False
    
    if not isinstance(data, dict):
        print(f"[FAIL] Expected dict, got {type(data)}")
        return False
    
    issues = []
    invalid_urls = []
    
    for career, career_data in data.items():
        if 'resources' not in career_data:
            issues.append(f"{career}: Missing 'resources' field")
        else:
            resources = career_data['resources']
            if not isinstance(resources, list):
                issues.append(f"{career}: 'resources' should be a list")
            else:
                for i, resource in enumerate(resources):
                    if 'title' not in resource:
                        issues.append(f"{career}[{i}]: Missing 'title'")
                    if 'url' not in resource:
                        issues.append(f"{career}[{i}]: Missing 'url'")
                    elif not validate_url(resource['url']):
                        invalid_urls.append(f"{career}[{i}]: Invalid URL: {resource.get('url')}")
                    if 'verified' not in resource:
                        issues.append(f"{career}[{i}]: Missing 'verified' field")
    
    if issues:
        print(f"[FAIL] Found {len(issues)} structural issues:")
        for issue in issues[:10]:
            print(f"   - {issue}")
    
    if invalid_urls:
        print(f"[WARN] Found {len(invalid_urls)} invalid URLs:")
        for issue in invalid_urls[:10]:
            print(f"   - {issue}")
    
    if not issues and not invalid_urls:
        total_resources = sum(len(cd['resources']) for cd in data.values() if 'resources' in cd)
        print(f"[PASS] Valid: {len(data)} career paths with {total_resources} total resources")
        return True
    
    return len(issues) == 0


def validate_roles(data_dir: Path) -> bool:
    """Validate roles.json"""
    print("\n" + "=" * 80)
    print("VALIDATING roles.json")
    print("=" * 80)
    
    filepath = data_dir / 'roles.json'
    data = load_json(filepath)
    if data is None:
        return False
    
    if not isinstance(data, list):
        print(f"[FAIL] Expected list, got {type(data)}")
        return False
    
    issues = []
    for i, role in enumerate(data):
        if 'title' not in role:
            issues.append(f"Role {i}: Missing 'title'")
        if 'coreSkills' not in role:
            issues.append(f"Role {i}: Missing 'coreSkills'")
        if 'tools' not in role:
            issues.append(f"Role {i}: Missing 'tools'")
    
    if issues:
        print(f"[FAIL] Found {len(issues)} issues:")
        for issue in issues[:10]:
            print(f"   - {issue}")
        return False
    
    print(f"[PASS] Valid: {len(data)} career roles defined")
    return True


def validate_certifications(data_dir: Path) -> bool:
    """Validate certifications.json"""
    print("\n" + "=" * 80)
    print("VALIDATING certifications.json")
    print("=" * 80)
    
    filepath = data_dir / 'certifications.json'
    data = load_json(filepath)
    if data is None:
        return False
    
    if not isinstance(data, list):
        print(f"[FAIL] Expected list, got {type(data)}")
        return False
    
    issues = []
    for i, cert_group in enumerate(data):
        if 'role' not in cert_group:
            issues.append(f"Item {i}: Missing 'role'")
        if 'certifications' not in cert_group:
            issues.append(f"Item {i}: Missing 'certifications'")
        else:
            certs = cert_group['certifications']
            if not isinstance(certs, list):
                issues.append(f"Item {i}: 'certifications' should be a list")
            else:
                for j, cert in enumerate(certs):
                    if 'name' not in cert:
                        issues.append(f"Item {i}, Cert {j}: Missing 'name'")
                    if 'provider' not in cert:
                        issues.append(f"Item {i}, Cert {j}: Missing 'provider'")
    
    if issues:
        print(f"[FAIL] Found {len(issues)} issues:")
        for issue in issues[:10]:
            print(f"   - {issue}")
        return False
    
    total_certs = sum(len(cg['certifications']) for cg in data if 'certifications' in cg)
    print(f"[PASS] Valid: {len(data)} role groups with {total_certs} total certifications")
    return True


def main():
    """Run all validations"""
    print("=" * 80)
    print("PathPilot AI Data Validation")
    print("=" * 80)
    
    data_dir = Path(__file__).parent / 'data'
    
    if not data_dir.exists():
        print(f"[FAIL] Data directory not found: {data_dir}")
        sys.exit(1)
    
    results = {
        'projects.json': validate_projects(data_dir),
        'verified_projects.json': validate_verified_projects(data_dir),
        'resources.json': validate_resources(data_dir),
        'verified_resources.json': validate_verified_resources(data_dir),
        'roles.json': validate_roles(data_dir),
        'certifications.json': validate_certifications(data_dir),
    }
    
    print("\n" + "=" * 80)
    print("VALIDATION SUMMARY")
    print("=" * 80)
    
    for filename, passed in results.items():
        status = "[PASS]" if passed else "[FAIL]"
        print(f"{status}: {filename}")
    
    all_passed = all(results.values())
    
    print("=" * 80)
    if all_passed:
        print("ALL VALIDATIONS PASSED")
        print("=" * 80)
        sys.exit(0)
    else:
        print("SOME VALIDATIONS FAILED")
        print("=" * 80)
        sys.exit(1)


if __name__ == '__main__':
    main()

# Made with Bob
